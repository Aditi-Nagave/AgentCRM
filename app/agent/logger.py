# app/agent/logger.py
def create_log(

        thought,

        action,

        observation,

        next_step
):

    return {

        "thought": thought,

        "action": action,

        "observation": observation,

        "next_step": next_step
    }