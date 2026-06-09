from flask import Flask, request, jsonify
from supabase import create_client
import os
from datetime import datetime, timezone

app = Flask(__name__)

supabase = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)

@app.route('/notify', methods=['POST'])
def receive_notification():
    payload = request.json or request.form.to_dict() or {}
    supabase.table("notifications").insert({
        "received_at": datetime.now(timezone.utc).isoformat(),
        "payload": payload
    }).execute()
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run()
