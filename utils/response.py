def success_response(message="Success", data=None, status=200):
    return {
        "success": True,
        "message": message,
        "data": data
    }, status


def error_response(message="Error", status=400):
    return {
        "success": False,
        "message": message,
        "data": None
    }, status