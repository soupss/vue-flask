<template>
    <button @click="deleteArticle">x</button>
    <h1>{{ article.title }}</h1>
    <p>uploaded <b>{{ article.created_at }}</b></p>
    <p>category:{{ article.category }}</p>
    <p>{{ article.description }}</p>
    <p>{{ article.price }}$</p>
</template>

<script>
export default {
    name: 'Article',
    props: {
        id: String
    },
    data() {
        return {
            article: {}
        }
    },
    methods: {
        deleteArticle() {
            this.$store.dispatch('deleteArticle', this.id)
                .then(() => this.$router.push('/articles'))
        }
    },
    created() {
        this.$store.dispatch('fetchArticle', this.id)
            .then(response => (this.article = response))
    }

}
</script>
