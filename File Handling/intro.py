def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if(flavor == "unknown"):
            raise ValueError("Unknown chai type")
    except ValueError as e:
        print(e)
    else:     #this else is a part of try block
        print(f"{flavor} chai is ready")
    finally:
        print("Next customer please")

serve_chai("unknown")
serve_chai("Masala Chai")