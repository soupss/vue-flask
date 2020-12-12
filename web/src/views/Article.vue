<template>
    <button @click="goToEditPage">Edit</button>
    <button @click="deleteArticle">Delete</button>
    <h1>{{ article.title }}</h1>
    <p>uploaded <b>{{ article.time_created }}</b></p>
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
        },
        goToEditPage() {
            this.$router.push('/articles/' + this.id + '/edit')
        }
    },
    created() {
        this.$store.dispatch('fetchArticle', this.id)
            .then(response => (this.article = response))
    }

}
</script>
