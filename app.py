from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')
@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)




def write_to_csv(data):
	with open('memories.csv', newline='',mode='a') as f:
		
		name = data['name']
		msg = data['message']
		csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,msg])

def write_to_csv(data):
	with open('memories.csv', newline='',mode='a') as f:
		
		name = data['name']
		msg = data['message']
		csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,msg])
		print(msg)
		return f.close()


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('index.html')
		except:
			print("Error")
	else:
		return 'Something went wrong'