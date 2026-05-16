from database import SessionLocal, TrainingSession
from model.lora_adapter import ScoreSyncLoRA
from storage.s3_storage import S3Storage

class TrainerService:
    def __init__(self):
        self.lora = ScoreSyncLoRA()
        self.s3 = S3Storage()

    def log_session(self, data: dict):
        db = SessionLocal()
        try:
            session = TrainingSession(
                user_id=data.get("user_id", 1),
                session_type=data.get("type", "pitch_practice"),
                accuracy=float(data.get("accuracy", 0.0)),
                tempo_stability=float(data.get("tempo_stability", 0.0)),
                repeat_count=int(data.get("repeat_count", 0)),
                duration_seconds=int(data.get("duration", 0)),
                error_types=data.get("error_types", {}),
                metadata=data.get("metadata", {})
            )
            db.add(session)
            db.commit()
            return {"status": "success", "session_id": session.id}
        finally:
            db.close()

    def train(self, adapter_name: str = "default"):
        # Implementation stub
        return {"status": "success", "message": "Training started"}