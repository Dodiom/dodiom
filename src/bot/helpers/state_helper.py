import logging
from enum import Enum, auto

from telegram.ext import CallbackContext


class State(Enum):
    """Enum for storing user states"""
    NONE = auto(),
    SUBMISSION = auto()
    TYPING_EXAMPLE = auto()
    CHOOSING_SUBMISSION_CATEGORY = auto()
    CHANGING_LANGUAGE = auto()
    REVIEWING = auto()


def clear_state(context: CallbackContext) -> None:
    set_state(context, State.NONE)
    logging.info("State cleared")


def set_state(context: CallbackContext, state: State) -> None:
    context.user_data["state"] = state
    logging.info("State set to: {state}", state=str(state))


def get_state(context: CallbackContext) -> State:
    if "state" in context.user_data:
        return context.user_data["state"]
    else:
        set_state(context, State.NONE)
        return State.NONE
