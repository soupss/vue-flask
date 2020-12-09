<template>
    <button @click="deleteThis">x</button>
    <h1>{{ title }}</h1>
    <small>{{ price }}$</small>
    <p>{{ description }}</p>
    <p>uploaded <b>{{ created_at }}</b></p>
</template>

<script>
export default {
    name: 'Shop Article',
    props: {
        title: String,
        description: String,
        price: Number,
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
                .then(_ => this.$emit('delete'))
        }
    }
}
</script>
