<template>
    <button @click="deleteThis">x</button>
    <h1>{{ title }}</h1>
    <small>({{ category }})</small>
    <p><b>{{ price }}$</b></p>
    <p>{{ description }}</p>
    <p>uploaded <b>{{ created_at }}</b></p>
</template>

<script>
export default {
    name: 'Article Preview',
    props: {
        title: String,
        description: String,
        price: Number,
        category: String,
        created_at: String,
        id: Number
    },
    emits: ['delete'],
    methods: {
        deleteThis() {
            const body = {}
            const requestOptions = {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(body)
            }
            fetch('http://localhost:5000/api/articles/'+this.id+'/', requestOptions)
                .then(() => this.$emit('delete'))
        }
    }
}
</script>
