export const handler = async (event: { name: string }) => {
    const result: string = event.name ? `Good Job ${event.name}!` : 'Good Job'
    return result
}