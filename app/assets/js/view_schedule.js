var scheduleTable = new Vue({
    el: '#scheduleTable',
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
        el: "#scheduleModal", 
        data: {
            header: "Schedule Name Here"
        }
})