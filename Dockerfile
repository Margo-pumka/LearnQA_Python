FROM python
WORKDIR /test-project
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=prod
CMD python -m pytest -s --alluredir=test_results /test_project/tests/