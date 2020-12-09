<template>
    <h1>Articles</h1>
    <p v-if="articles.length === 0">No articles</p>
    <article-element v-for="article in articles" :key="article.id" :="article" @delete="loadArticles"></article-element>
</template>

<script>
import Article from '@/components/Article.vue'

export default {
    name: 'Articles',
    components: {
        'article-element': Article
    },
    data() {
        return {
            articles: []
        }
    },
    methods: {
        loadArticles() {
            fetch('http://localhost:5000/api/articles/')
                .then(response => response.json())
                .then(json => (this.articles = json.articles))
        }
    },
    created() {
        this.loadArticles()
    }
}
</script>
