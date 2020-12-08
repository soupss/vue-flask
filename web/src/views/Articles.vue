<template>
    <h1>Articles</h1>
    <p v-if="articles.length === 0">No articles</p>
    <shop-article v-for="article in articles" :="article" @delete="loadArticles"></shop-article>
</template>

<script>
import ShopArticle from '@/components/ShopArticle.vue'

export default {
    name: 'Articles',
    components: {
        'shop-article': ShopArticle
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
