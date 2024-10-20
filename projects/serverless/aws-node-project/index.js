module.exports.handler = async (event) => {
  return {
    statusCode: 200,
    body: JSON.stringify(
      {
        message: 'Testing from local test func!',
        input: event,
      },
      null,
      2
    ),
  };
};
