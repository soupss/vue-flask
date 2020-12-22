<template>
    <!--
        TODO: style no articles msg
    -->
    <p v-if="articles.length === 0 && articles.length === 0">No articles</p>
    <div class="d-flex flex-wrap p-2 justify-content-center">
        <ArticlePreview v-for="article in articles" :key="article.id" :article="article"/>
    </div>
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
        created() {
                this.$store.dispatch('fetchArticles')
                    .then(result => (this.articles = result))
            }
    }
</script>
