<template>
    <h1>New Article</h1>
    <form @submit="createArticle">
        <label for="title">Enter Title</label>
        <input v-model.lazy="article.title" id="title" placeholder="A green car" required/>
        <label for="description">Enter description</label>
        <textarea v-model.lazy="article.description" rows="4" cols="50" id="description" placeholder="It is green..." required/>
        <label for="price">Enter price in $</label>
        <input v-model.number="article.price" id="price" type="number" min="0" required/>
        <label for="category">Select category</label>
        <select v-model.lazy="article.category" id="category">
            <option value="vehicles">Vehicles</option>
            <option value="clothes">Clothes</option>
            <option value="other">Other</option>
        </select>
        <button type="submit">create</button>
    </form>
</template>

<script>
export default {
    name: 'New Article',
    data() {
        return {
            article: {
                title: '',
                description: '',
                price: 0,
                category: 'other'
            }
        }
    },
    methods: {
        createArticle() {
            this.$store.dispatch('createArticle', this.article)
                .then(() => this.$router.push('/articles'))
        }
    }
}
</script>

<style>
form label, input, select {
    display: block;
}
form textarea {
    resize: none;
}
</style>
