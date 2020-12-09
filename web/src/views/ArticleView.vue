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
        loadArticle() {
            fetch('http://localhost:5000/api/articles/'+this.id+'/')
                .then(response => response.json())
                .then(json => (this.article = json.article))
        },
        deleteArticle() {
            const body = {}
            const requestOptions = {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(body)
            }
            fetch('http://localhost:5000/api/articles/'+this.id+'/', requestOptions)
                .then(() => this.$router.push('/articles'))
        }
    },
    created() {
        this.loadArticle()
    }

}
</script>
