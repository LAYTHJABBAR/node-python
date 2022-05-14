const express = require('express')
const { spawn } = require('child_process')
const app = express()
const port = 4000
app.use(express.urlencoded({extended: true}));
app.use(express.json())


app.get('/', (req, res) => {
  let dataToSend
  let largeDataSet = []
  // spawn new child process to call the python script
  const python = spawn('python3', ['script3.py'])

  // collect data from script
  python.stdout.on('data', function (data) {
    console.log('Pipe data from python script ...')
    //dataToSend =  data;
    largeDataSet.push(data)
  })

  // in close event we are sure that stream is from child process is closed
  python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`)
    // send data to browser
    res.send(largeDataSet.join(''))
  })
})

app.post('/switchstatus', (req,res) => {
  try{
     console.log("watch the value",req.body.status)
    // let status = Number(req.body.status);
    // console.log(status)
    const python = spawn('python3', ['script5.py', req.body.status])
   
    python.stdout.on('data', function (data) {
    console.log(JSON.parse(data))
   })
   res.send({message: req.body.status});
  }catch(err){
    res.status(500).send({status: err})

  }
})

app.listen(port, () => {
  console.log(`App listening on port ${port}!`)
})
