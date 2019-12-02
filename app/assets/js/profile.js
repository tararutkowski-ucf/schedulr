var profile = new Vue({
    el: '#profile',
    data: {
        form: {
            FirstName:'',
            LastName:'',
            Email:''
        },
    },
    mounted: function() {
        axios.get('/myinfo')
            .then(response=> {
                console.log(response);
                this.form.FirstName = response.data.FirstName;
                this.form.LastName = response.data.LastName;
                this.form.Email = response.data.Username;
            })
            .catch(error => {
                console.log(error);
            })
    }
})