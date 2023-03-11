import { useEffect, useState } from 'react';
import { useInView } from 'react-intersection-observer';

const defaultTextClass = 'tracking-widest';

function MainIntroduce() {
  const { ref, inView } = useInView({
    threshold: 0,
  });
  const [textClass, setTextClass] = useState(defaultTextClass);
  useEffect(() => {
    setTextClass(
      inView
        ? `animate-[showUp_1s_ease-in-out] ${defaultTextClass}`
        : defaultTextClass,
    );
  }, [inView]);
  return (
    <div className="my-20" ref={ref}>
      <h1 className="text-2xl mb-20">Test</h1>
      <p className={textClass}>
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ab beatae
        libero cum ut veritatis quis facere ipsam, consectetur quia inventore
        aspernatur odit ipsa voluptatum hic iusto, numquam quibusdam vitae modi
        sed eum recusandae neque perferendis pariatur. Dolorum, necessitatibus
        veniam tempore placeat est consectetur nihil ullam accusamus, atque
        soluta molestiae modi veritatis! Consequatur beatae eum animi
        accusantium mollitia error aperiam, dolor ducimus omnis libero qui
        iusto, possimus nostrum tempore veniam tempora recusandae asperiores
        voluptatum quia sapiente. Commodi, libero? Quaerat assumenda ab, magni
        consectetur nesciunt exercitationem cupiditate corporis sed ea dolores
        velit, iusto vero recusandae eveniet totam voluptates possimus eaque
        fugit doloremque eos officia excepturi hic sapiente. Quae, eligendi
        optio et, sunt dolorem quisquam vero atque eius adipisci, ea officia
        consequuntur dicta rem dolor eveniet consectetur quos odit voluptatem
        fugiat saepe. Consequatur fugiat dolorem nemo neque, veritatis suscipit
        nulla autem hic numquam perspiciatis? Magni ad voluptatem nulla, quasi
        dignissimos error labore, eos dolorum minus consequatur suscipit. Iusto
        nostrum culpa deleniti commodi! Nesciunt culpa sed quasi odit natus,
        animi ratione fugiat maxime est optio incidunt nulla distinctio sapiente
        aspernatur provident eos unde, quae minima assumenda earum recusandae
        dolores ex? Tempore laudantium magni eos nihil facere illo, nobis
        incidunt inventore excepturi, odio eligendi beatae!
      </p>
    </div>
  );
}

export default MainIntroduce;
