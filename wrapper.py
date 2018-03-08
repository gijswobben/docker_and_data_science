# Imports
import json
import numpy
import pickle

from nameko.web.handlers import http


class IrisClassifierService(object):
	""" This class wraps the model and is used by Nameko
		to start the service.
	"""

	name = 'iris_classifier_service'
	model = pickle.load(open('models/iris_classifier.pickle', 'rb'))


	def predict(self, data):
		""" Method that will make the actual prediction.
		"""

		# Convert the data into the same format as during training (numpy.array)
		data = numpy.array(data)

		# Use the model to predict the class
		return self.model.predict(data)


	@http('POST', '/classify')
	def classify(self, request):
		""" This method will handle incoming data,
			run it through the model and return the
			classified output.
		"""

		try:

			# Get the data from the request
			new_data = request.get_data(as_text=True)

			# Parse the input data (JSON)
			new_data = json.loads(new_data)

			# Make the prediction
			prediction = self.predict(new_data)

			# Return the prediction
			return json.dumps({
				'status': 'success',
				'message': 'Classified input data',
				'predictions': prediction.tolist()
			})

		except ValueError:

			# Send a message back when the input is not valid JSON
			return json.dumps({
				'status': 'failed',
				'message': 'Input is not valid JSON data'
			})

		except Exception as e:

			# Send a message back when another error occurs (with the error message)
			return json.dumps({
				'status': 'failed',
				'message': 'Some error occured',
				'error': e
			})
