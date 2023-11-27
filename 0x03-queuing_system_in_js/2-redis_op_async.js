import { createClient } from 'redis';

const client = createClient()

client.on('error', err => console.log('Redis client not connected to the server: ', err))

client.on('connect', () => {
      console.log('Redis client connected to the server')
  });


const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, (err, reply) => {
        console.log(`reply: ${reply}`) // ok
    })
}

async function displaySchoolValue (schoolName) {
    await client.get(schoolName, (err, reply) => {
        console.log(reply) // log the value of key schoolName
    })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
