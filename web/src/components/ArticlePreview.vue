<template>
    <a id="header" @click="goToArticlePage" class="m-2 rounded-3 shadow-lg"
        @mouseover="hover = true"
        @mouseleave="hover = false">
        <div class="bg-primary text-white rounded-top p-2">
            <h3 class="d-inline mb-0 align-middle me-5">{{ article.title }}</h3>
        </div>
        <div id="body" class="p-2 rounded-bottom" :class="{'bg-primary':hover, 'text-white':hover}">
            <p>
                <i class="fas fa-tshirt align-middle"></i>
                <span class="ms-1">{{ article.category }}</span>
            </p>
            <p>
                <small><strong>{{ article.time_created }}</strong></small>
            </p>
            <p>
                {{ article.price }}$
                <i class="fas fa-tag fa-xs"></i>
            </p>
        </div>
    </a>
</template>

<script>
export default {
    name: 'Article Preview',
    data() {
        return {
            hover: false
        }
    },
    props: {
            article: Object
    },
    methods: {
        goToArticlePage() {
            this.$router.push('/articles/'+this.id)
        }
    }
}
</script>

<style scoped>
a {
    text-decoration: none;
    cursor: pointer;
}
a:hover {
    background-color: ;
}
p {
    margin-bottom: 0;
}
</style>
