#!/usr/bin/env python3
import sys
import numpy as np
from flask import Flask, request, jsonify
import onnxruntime as ort

app = Flask(__name__)
session = None

@app.route('/infer', methods=['POST'])
def infer():
    data = request.json.get("obs", [])
    obs = np.array(data, dtype=np.float32)
    # [batch, ...] shape if needed
    obs = np.expand_dims(obs, axis=0)
    outputs = session.run(None, {"obs": obs})
    # outputs: [action, value], each is a numpy array
    # For discrete action, let's pick argmax
    action_logits = outputs[0]
    action = int(np.argmax(action_logits, axis=1)[0])
    return jsonify({"action": action})

if __name__ == '__main__':
    model_path = sys.argv[1] if len(sys.argv) > 1 else "ddx_model.onnx"
    print(f"[DDx Inference] Loading ONNX model: {model_path}")
    session = ort.InferenceSession(model_path)
    app.run(host="0.0.0.0", port=8500, debug=False)
