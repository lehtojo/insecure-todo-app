import django.contrib.sessions.backends.db as db

class SessionStore(db.SessionStore):
	counter = 0

	def _get_new_session_key(self):
		while True:
			key = 'session-' + str(SessionStore.counter)
			SessionStore.counter += 1

			if not self.exists(key):
				return key
