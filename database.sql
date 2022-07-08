SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `minibank`
--

DELIMITER $$
--
-- Procedimentos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `SP_ALTERAR_SALDO` (IN `p_id_usuario` INT, IN `p_valor` DECIMAL, IN `p_valor_alterado` DECIMAL, IN `p_tipo_movimento` INT)   BEGIN
	UPDATE usuarios SET SALDO = p_valor WHERE ID = p_id_usuario;
    INSERT INTO extrato (ID_USUARIO, TIPO_MOVIMENTO, VALOR) VALUES (p_id_usuario, p_tipo_movimento, p_valor_alterado);
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `extrato`
--

CREATE TABLE `extrato` (
  `ID` int NOT NULL,
  `ID_USUARIO` int NOT NULL,
  `DH_MOVIMENTO` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `TIPO_MOVIMENTO` int NOT NULL,
  `VALOR` decimal(15,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_movimento`
--

CREATE TABLE `tipo_movimento` (
  `ID_TIPOMOVIMENTO` int NOT NULL,
  `DESCRICAO` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `tipo_movimento`
--

INSERT INTO `tipo_movimento` (`ID_TIPOMOVIMENTO`, `DESCRICAO`) VALUES
(1, 'DEPOSITO'),
(2, 'SAQUE');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `ID` int NOT NULL,
  `NOME` varchar(45) NOT NULL,
  `CPF` varchar(11) NOT NULL,
  `SALDO` decimal(15,2) NOT NULL DEFAULT '0.00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `extrato`
--
ALTER TABLE `extrato`
  ADD PRIMARY KEY (`ID`);

--
-- Índices para tabela `tipo_movimento`
--
ALTER TABLE `tipo_movimento`
  ADD PRIMARY KEY (`ID_TIPOMOVIMENTO`);

--
-- Índices para tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `extrato`
--
ALTER TABLE `extrato`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tipo_movimento`
--
ALTER TABLE `tipo_movimento`
  MODIFY `ID_TIPOMOVIMENTO` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
