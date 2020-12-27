<!--
    This component is used to both create and edit articles

    If the id prop is supplied, edit the corresponding article
    If no id is supplied, create a new article
-->
<template>
    <h1>New Article</h1>
    <form>
        <label for="title">Enter Title</label>
        <input v-model.lazy="article.title" id="title" placeholder="A green car" required/>
        <label for="description">Enter description</label>
        <textarea v-model.lazy="article.description" rows="4" cols="50" id="description" placeholder="It is green..."/>
        <label for="price">Enter price in $</label>
        <input v-model.number="article.price" id="price" type="number" min="0" required/>
        <label for="category">Select category</label>
        <select v-model.lazy="article.category" id="category">
            <option value="vehicles">Vehicles</option>
            <option value="clothes">Clothes</option>
            <option value="other">Other</option>
        </select>
        <button v-if="edit" @click="updateArticle" type="submit">update</button>
        <button v-else @click="createArticle" type="submit">create</button>
    </form>
</template>

<script>
export default {
    name: 'New Article',
    props: {
        id: String
    },
    data() {
        return {
            edit: false,
            article: {
                id: this.id,
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
                .then(() => this.$router.go(-1))
        },
        updateArticle() {
            this.$store.dispatch('updateArticle', this.article)
                .then(() => this.$router.go(-1))
        }
    },
    created() {
        if(this.id !== undefined){
            // this form now edits an article
            this.edit = true
            // TODO: check if article with this id exists
            this.$store.dispatch('fetchArticle', this.id)
                .then(response => (this.article = response))
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
