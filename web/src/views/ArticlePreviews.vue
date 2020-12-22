<template>
    <!--
        TODO: style no articles msg
    -->
    <p v-if="articles.length === 0 && mock_articles.length === 0">No articles</p>
    <div class="d-flex flex-wrap p-2 justify-content-center">
        <ArticlePreview v-for="article in mock_articles" :key="article.id" :article="article"/>
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
            articles: [],
            mock_articles: [
                {
                    'id': 1,
                    'title': 'A Green Car',
                    'description': 'This is a fine green car.',
                    'price': 3799,
                    'category': 'Vehicles',
                    'time_created': 'Today'
                },
                {
                    'id': 2,
                    'title': 'Sock',
                    'description': 'A fine sock.',
                    'price': 23,
                    'category': 'Clothes',
                    'time_created': 'Today'
                },
                {
                    'id': 3,
                    'title': 'Dog Named Hubert',
                    'description': 'Hubert is nice.',
                    'price': 900,
                    'category': 'Pets',
                    'time_created': '3 days ago'
                },
                {
                    'id': 4,
                    'title': '1000 FPS Flatscreen TV',
                    'description': 'Best of the best!',
                    'price': 2000,
                    'category': 'Other',
                    'time_created': '1 year ago'
                },
                {
                    'id': 5,
                    'title': 'My House',
                    'description': 'I\'m selling my house because I want to.',
                    'price': 8000000,
                    'category': 'Other',
                    'time_created': 'Yesterday'
                }
                ]
            }
        },
        created() {
                this.$store.dispatch('fetchArticles')
                    .then(result => (this.articles = result))
            }
    }
</script>
