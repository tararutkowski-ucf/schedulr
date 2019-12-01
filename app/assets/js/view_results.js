var scheduleTable = new Vue({
    el: '#viewResults_scheduleTable',
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
        el: "#viewResults_scheduleModal", 
        data: {
            header: "Schedule Name Here"
        }
})