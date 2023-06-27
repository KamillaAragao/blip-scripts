import csv
from blip_session import BlipSession

# Fill with bot authorization key and user identity
BOT_AUTHORIZATION = "Key YmFuY29wYW5yb3V0ZXJwcm9tbzpzUzlIUW1zWnE5aG9ZM3ZmRUxlRA=="
CONTEXT_VAR = ["master-state", "stateid"]

DELETE_METHOD = "delete"
GET_METHOD = "get"

if BOT_AUTHORIZATION == "":
    print(
        "[ERROR] Reason: : must have a valid bot_authorization key."
    )
    exit(-1)


def create_all_context_request(user_id):
    return {
        "method": GET_METHOD,
        "to": "postmaster@msging.net",
        "uri": f"/contexts/{user_id}",
    }


def delete_specific_context_variable(user_id, context_var):
    return {
        "method": DELETE_METHOD,
        "to": "postmaster@msging.net",
        "uri": f"/contexts/{user_id}/{context_var}",
    }


if __name__ == "__main__":
    blipSession = BlipSession(BOT_AUTHORIZATION, "bancopan")

    with open("2023-04-11-Bloquear.xlsx - Bloquear.csv", encoding="utf-8") as archive:
        table = csv.reader(archive, delimiter=",")

        for user_id in table:
            res_context = blipSession.process_command(
                create_all_context_request(user_id[0])
            )

            for context_var in CONTEXT_VAR:
                if res_context.get("status") == "success":
                    res__delete_context = blipSession.process_command(
                        delete_specific_context_variable(user_id[0], context_var)
                    )
                    if res__delete_context["status"] == "success":
                        print(f"Deleted context var")
                    else:
                        print(
                            f'[ERROR] Reason: {res__delete_context["reason"]["description"]}'
                        )

                    print("Finished")