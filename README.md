Example Repo to show issue with response character sets

> pip install --upgrade pip
> pip install poetry
> poetry install
> poetry shell

In first shell run: 
> uvicorn server:app

In second shell run: 
> python run_test.py

The downloaded file saved_output.pdf should be the same as the send file (example_pdf.pdf)
