<template>
    <h1>Articles</h1>
    <p v-if="articles.length === 0">No articles</p>
    <ArticlePreview v-for="article in articles" :key="article.id" :="article"/>
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
            articles: [],
        }
    },
    created() {
        this.$store.dispatch('fetchArticles')
            .then(result => (this.articles = result))
    }
}
</script>
