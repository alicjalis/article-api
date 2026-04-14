from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserOut
from app.core.deps import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/me/subscribe", response_model=UserOut)
def subscribe(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    current_user.is_subscribed = True
    db.commit()
    db.refresh(current_user)
    return current_user


@router.delete("/me/subscribe", response_model=UserOut)
def unsubscribe(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    current_user.is_subscribed = False
    db.commit()
    db.refresh(current_user)
    return current_user


@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user