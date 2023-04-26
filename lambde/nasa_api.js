const AWS = require("aws-sdk");
const dynamoDb = new AWS.DynamoDB.DocumentClient();
const https = require('https')
let url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"   

exports.handler = async function(event) {
    let params = await new Promise(function(resolve, reject) {
    https.get(url, (res) => {
        let data = "";
        res.on('data', (d) => { data += d })
        res.on('end', () => {
            let finalData = JSON.parse(data);
            const params = {
            TableName: "amilosevic-nasa-2",
            Item: {
                title: finalData.title,
                url: finalData.url,
                explanation: finalData.explanation,
                },
            };
            resolve(params);
            //resolve(finalData);
        });
        //resolve(res)
      }).on('error', (e) => {
        reject(Error(e))
      })
    })
    console.log(params);
    try {
        await dynamoDb.put(params).promise();
        return {
         statusCode: 200,
         body: JSON.stringify({
           message: "Item created!",
         }),
        };
    } catch (error) {
     console.error(error);
     return {
       statusCode: error.statusCode,
       body: JSON.stringify({
        message: "Item not created!",
      }),
    };
  }
}