<template>
    <h1>New Article</h1>
    <form @submit="createArticle">
        <label for="title">Enter Title</label>
        <input v-model.lazy="title" id="title" placeholder="A green car" required/>
        <label for="description">Enter description</label>
        <textarea v-model.lazy="description" rows="4" cols="50" id="description" placeholder="It is green..." required/>
        <label for="price">Enter price in $</label>
        <input v-model.number="price" id="price" type="number" min="0" required/>
        <button type="submit">create</button>
    </form>
</template>

<script>
export default {
    name: 'New Article',
    data() {
        return {
            title: '',
            description: '',
            price: 0,
        }
    },
    methods: {
        createArticle() {
            const article = {
                title: this.title,
                description: this.description,
                price: this.price
            }
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(article)
            }
            fetch('http://localhost:5000/api/articles/', requestOptions)
        }
    }
}
</script>

<style>
form label, input {
    display: block;
}
form textarea {
    resize: none;
}
</style>
