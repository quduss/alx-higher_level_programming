#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completedCounts = {};

    // Initialize completedCounts with userIds from 1 to 10
    for (let userId = 1; userId <= 10; userId++) {
      completedCounts[userId] = 0;
    }

    // Count completed todos for each userId
    todos.forEach(todo => {
      if (todo.completed) {
        completedCounts[todo.userId]++;
      }
    });

    console.log(completedCounts);
  }
});
