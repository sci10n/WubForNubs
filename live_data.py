import database_helper


class LiveData(object):
    def __init__(self, email):
        self.email = email

        self._fill_data()

    def _fill_data(self):
        self.num_of_signedup_users = len(database_helper.signed_up_users())
        self.num_of_messages = len(database_helper.get_messages(self.email))
        self.num_of_signin_users = len(database_helper.signed_in_users())

    def json(self):
        return {"signedup": self.num_of_signedup_users,
                "signedin": self.num_of_signin_users,
                "messages": self.num_of_messages}