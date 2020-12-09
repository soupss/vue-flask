<template>
    <h1>Articles</h1>
    <p v-if="articles.length === 0">No articles</p>
    <ArticlePreview v-for="article in articles" :key="article.id" :="article" @delete="loadArticles"/>
</template>

<script>
import ArticlePreview from '@/components/ArticlePreview.vue'

export default {
    name: 'Article Previews',
    components: {
        'ArticlePreview': ArticlePreview
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
