FROM public.ecr.aws/lambda/python:3.11

COPY index.py ${LAMBDA_TASK_ROOT}

CMD ["index.lambda_handler"]