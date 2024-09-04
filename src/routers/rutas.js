import { createRouter, createWebHistory} from "vue-router";
import tecnicos from "@/components/tecnicos.vue"
import users from "@/components/users.vue"
import celulares from "@/components/celulares.vue";
import spareParts from "@/components/spare-parts.vue";

const routes=[
    {
        path:'/users',
        name: 'usuarios',
        component: users
    },
    {
        path:'/tec',
        name: 'tecnicos',
        component: tecnicos
    },
    {
        path:'/phones',
        name: 'phones',
        component: celulares
    },
    {
        path: '/spareparts',
        name: 'spareparts',
        component: spareParts
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
