class outOfIngerdientsError(Exception):
    pass

def serve_chai(chai_type):
    if chai_type == "unknown":
        raise outOfIngerdientsError("No chai available")
    print("Next customer please")

serve_chai("Masala Chai")
serve_chai("unknown")