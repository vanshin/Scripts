var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!',
    todos: [
      {text: 'xuexi'},
      {text: 'vand'},
      {text: 'dfgret'}
    ],
    
  },
  methods: {
      reverseMessage:function() {
        this.message = "vanwrefr"
      }
    }
  
})

