#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    try:
        # Correct input types
        if not isinstance(template, str):
            print("Error: template must be a string.")
            return

        if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
            print("Error: attendees must be a list of dictionaries.")
            return

        # No empty inputs
        if template.strip() == "":
            print("Template is empty, no output files generated.")
            return

        if len(attendees) == 0:
            print("No data provided, no output files generated.")
            return

        # Iterate over the list of attendees and replace the placeholders
        for i, attendee in enumerate(attendees, start=1):
            try:
                output = template

                # Replace placeholders using .replace()
                output = output.replace("{name}", str(attendee.get("name", "N/A")))
                output = output.replace("{event_title}", str(attendee.get("event_title", "N/A")))
                output = output.replace("{event_date}", str(attendee.get("event_date", "N/A")))
                output = output.replace("{event_location}", str(attendee.get("event_location", "N/A")))

                filename = f"output_{i}.txt"

                # Check if file exists
                if os.path.exists(filename):
                    print(f"Warning: {filename} already exists. Overwriting.")

                # Write to file with error handling
                with open(filename, "w") as file:
                    file.write(output)

            except Exception as e:
                print(f"Error processing attendee {i}: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")