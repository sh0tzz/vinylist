const app = Vue.createApp({
    data() {
        return {
            title: 'Compiler Dragon Book',
            author: 'Jan Grdanjski',
            age: 16,
            val: null,
            showVal: false
        }
    },
    methods: {
        increment() {
            this.age++
        },
        decrement() {
            this.age--
        }
    },
    components: {
        'p-slider': primevue.slider,
        'p-button': primevue.button,
        'p-menubar': primevue.menubar,
        'p-inputtext': primevue.inputtext
    }
})

app.use(primevue.config.default).mount('#app')