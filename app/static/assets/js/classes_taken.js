var classTable = new Vue({
    el: '#classesTaken_classTable',
    data: {
        users:[]
    },
    mounted: function() {
        axios.get('https://jsonplaceholder.typicode.com/users')
            .then(response=> {
                this.users = response.data;
                console.log(response);
            })
            .catch(error => {
                console.log(error);
            })
    }
})

var scheduleModal = new Vue({
        el: "#classesTaken_addClassModal", 
        data: {
        users:[]
    },
    mounted: function() {
        axios.get('https://jsonplaceholder.typicode.com/users')
            .then(response=> {
                this.users = response.data;
                console.log(response);
            })
            .catch(error => {
                console.log(error);
            })
    }
})