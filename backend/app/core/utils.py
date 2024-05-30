def custom_message_generator(milestone_name: str, achieved: bool) -> str:
    if achieved:
        return f"Congratulations! Your child has achieved the milestone: {milestone_name}"
    else:
        return f"Reminder: Your child is expected to achieve the milestone: {milestone_name}"
