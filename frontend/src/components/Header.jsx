function Header() {
  return (
    <div
        style={{
            display: "flex",
            justifyContent: "flex-end"
        }}
    >
        {
            ["Demo", "About", "Contact"].map((page, key)=>(
                <h2
                    key={key}
                    style={{
                        margin: "1em"
                    }}
                >
                    {page}
                </h2>
            ))
        }
    </div>
  )
}

export default Header