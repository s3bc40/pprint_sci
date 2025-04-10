import { WagmiPlugin } from '@wagmi/vue'
import { config } from '../wagmi.config'


export default defineNuxtPlugin(nuxtApp => {
    nuxtApp.vueApp.use(WagmiPlugin, { config })
})
