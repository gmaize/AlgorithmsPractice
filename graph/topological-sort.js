const Node = require('./Node')

const zero = new Node(0)
const one = new Node(1)
const two = new Node(2)
const three = new Node(3)
const four = new Node(4)
const five = new Node(5)
const six = new Node(6)
const nodes = [zero, one, two, three, four, five]

five.addNeighbor(zero)
five.addNeighbor(two)
four.addNeighbor(zero)
four.addNeighbor(one)
two.addNeighbor(three)
three.addNeighbor(one)

function topoSort(nodes) {
    const result = []
    const visited = {}
    for (var node of nodes) {
        visit(node, visited, result)
    }
    return result.reverse()
}

const sorted = topoSort(nodes)
console.log(sorted.map(node => node.id))

function visit(node, visited, result) {
    if (visited[node.id]) return
    visited[node.id] = true
    for (var neighbor of node.neighbors) {
        visit(neighbor, visited, result)
    }
    result.push(node)
}