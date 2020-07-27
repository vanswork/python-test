# run.py

import os
from project import app

#  app.run()
# app.run(debug=True)

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=False)


